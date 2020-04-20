---
title: Python + AWS Lambda + Graphene + SQLAlchemy
date: 2016-01-08 15:04:23
category: architecture
tags: [serverless python graphql]

layout: page
---

```sh
rm -rf _package*
mkdir _package
cd _package && pip install -r ../requirements.txt --target .
zip -r9 ../_package.zip .
cd .. && zip -g _package.zip main.py
rm -rf _package
```

requirements.txt
```txt
graphene[sqlalchemy]
sqlalchemy
flask
flask_graphql
psycopg2
```

main.py
```python
#!/usr/bin/env python

import os
import json
from flask import Flask
from flask_graphql import GraphQLView
import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType, utils
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Sequence, func, create_engine
from sqlalchemy.orm import backref, relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

################################## DATABASE #################################

POSTGRES_CONNECTION_STRING = os.environ.get('POSTGRES_CONNECTION_STRING')

engine = create_engine(POSTGRES_CONNECTION_STRING, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                     autoflush=False,
                     bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
  # import all modules here that might define models so that
  # they will be registered properly on the metadata.  Otherwise
  # you will have to import them first before calling init_db()
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)
  db_session.commit()

#############################################################################

################################## MODELS ###################################

class UserModel (Base):
  __tablename__ = 'users'
  id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
  name = Column(String)
  balance = Column(Integer)

#############################################################################


################################## SCHEMA ###################################

# Query #########################
class User(SQLAlchemyObjectType):
  class Meta:
    model = UserModel

class Query(graphene.ObjectType):

  hello = graphene.String()
  def resolve_hello(self, info):
    return "Hello World!"

  users = graphene.List(User)
  def resolve_users(self, info):
    query = User.get_query(info)
    return query.all()

################################

# Mutation #####################
class AddUser(graphene.Mutation):
  class Arguments:
      name = graphene.String()
      balance = graphene.Int()

  user = graphene.Field(User)
  def mutate(self, info, name, balance):
    user = UserModel(name=name, balance=balance)
    db_session.add(user)
    db_session.commit()
    return AddUser(user=user)

class Transfer(graphene.Mutation):
  class Arguments:
    userIdTo = graphene.Int()
    userIdFrom = graphene.Int()
    amount = graphene.Int()

  ok = graphene.Boolean()

  def mutate(self, info, userIdTo, userIdFrom, amount):
    ok = False
    userFrom = db_session.query(UserModel).filter(UserModel.id == userIdFrom).first()
    if (userFrom == None):
      raise GraphQLError('No user exists with id: ' + str(userIdFrom))

    userTo = db_session.query(UserModel).filter(UserModel.id == userIdTo).first()
    if (userTo == None):
      raise GraphQLError('No user exists with id: ' + str(userIdTo))

    if (userFrom.balance < amount):
      raise GraphQLError('Transferor does not have enough amount')

    try:
      userFrom.balance -= amount
      userTo.balance += amount
      db_session.commit()
    except exc:
      print (exc)
      raise Exception('Unexpected error')

    return Transfer(ok=True)

class Mutation(graphene.ObjectType):
  addUser = AddUser.Field()
  transfer = Transfer.Field()
##################################

schema = graphene.Schema(query=Query, mutation=Mutation)
#############################################################################


################################ FLASK APP ##################################
app.add_url_rule('/', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.teardown_appcontext
def shutdown_session(exception=None):
  db_session.remove()

#############################################################################

################################## EXECUTION ##################################

if os.environ.get('LAMBDA_LOCAL_DEVELOPMENT') == '1':
  if __name__ == '__main__':
    if os.environ.get('DATABASE_INIT') == '1':
      init_db()
    app.run()
#############################################################################

############################ GRAPHQL HANDLER ################################
def graphqlHandler(eventRequestBody, context = {}):

  try:
    requestBody = json.loads(eventRequestBody)
  except:
    requestBody = {}
  query = ''
  variables = {}
  if ('query' in requestBody):
    query = requestBody['query']
  if ('variables' in requestBody):
    variables = requestBody['variables']
  executionResult = schema.execute(query, variables=variables)

  responseBody = {
    "data": dict(executionResult.data) if executionResult.data != None else None,
  }
  if (executionResult.errors != None):
    responseBody['errors'] = []
    for error in executionResult.errors:
      responseBody['errors'].append(str(error))
  return responseBody

######################### LAMBDA HANDLER ####################################

responseHeaders = {
  'Content-Type': 'application/json',
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, GET, OPTIONS, PUT, DELETE",
  "Access-Control-Allow-Headers": "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization",
}

def lambda_handler(event, context):
  httpMethod = event.get('httpMethod')
  if (httpMethod == 'OPTIONS'):
    return {
      'statusCode': 200,
      'headers': responseHeaders,
      'body': ''
    }
  requestBody = event.get('body')
  responseBody = graphqlHandler(requestBody, context)
  return {
    'statusCode': 200,
    'headers': responseHeaders,
    'body': json.dumps(responseBody)
  }
    

###############################################################################
```


More instructions:
https://github.com/hasura/graphql-serverless/tree/master/aws-python/graphene-sqlalchemy
