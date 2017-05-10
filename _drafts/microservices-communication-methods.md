Communication between microservices allows us to build complex behaviors out of simple components. Most people tend to think of webservices when thinking of microservices however there are a number of other communication methods which are applicable in different situations.

### What does a communication method need
In order to use a specific communication method for talking between microservices the method must meet some criteria:

#### Deployment independence
The entire microservice (including any communication components) must be able to be deployed without orchestration with other services. Similarly the deployment of a consuming service must not necessitate a change from the provider. Or to think of it simply you must be able to deploy both provider and consumer without thinking of the other.

#### Versioned
A communication method must support versioning in order to allow for changes in the contracts.

### Communication characteristics
Internal vs external, synchronous vs asynchronous,

### HTTP Requests
The most common method of microservice communication is via HTTP webservices. This is probably because its familiar for developers using web stacks, and can be used both for services in you network as well as external access. HTTP is by nature synchronous (request-response).



### Message passing
Message passing is a common technique for asynchronous communication with microservices. This involves publishing a message which another microservice can subscribe to.
Message passing generally occurs over a trusted medium (eg the messaging system)

### Webhook subscriptions
Webhooks are an HTTP version of pub/sub message passing. While most messaging systems require all direct users of the system to be trusted, webhooks work well for pub/sub between endpoints which don't implicitly trust each other. For example between services maintained by different organisations.


### Runtime plugins
Runtime plugins can be used as a communication method with microservices under certain situations.
