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

#### Implementation
An HTTP communication method is implemented by the providing service creating an HTTP endpoint at a specific URL. Under this URL resources and methods exist which may be called by another service. The HTTP endpoint itself is normally not secured however security may be introduced by the service to enforce specific authorisations that may be relevant.

#### Security
Ideally authentication should not be performed directly by the service, rather a signed token should be passed with the request which allows the service to perform any required authorisation checks.

#### Versioning
HTTP communication methods usually achieve versioning by providing multiple

#### Deployment independence

### Message passing
Message passing is a common technique for asynchronous communication with microservices. This involves publishing a message which another microservice can subscribe to.
Message passing generally occurs over a trusted medium (eg the messaging system)

### Webhook subscriptions
Webhooks are an HTTP version of pub/sub message passing. While most messaging systems require all direct users of the system to be trusted, webhooks work well for pub/sub between endpoints which don't implicitly trust each other. For example between services maintained by different organisations.


### Runtime plugins
Runtime plugins can be used as a communication method with microservices under certain situations. I think most developers wouldn't even consider runtime plugins in microservice environments as most runtime techniques introduce significant coupling. However with a little cleverness this can be avoided.

![Runtime plugins]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/runtime-microservice-plugin.png)

There are two important components when using runtime microservice plugins, which are to do with versioning; *the consumer should not need to be changed when the provider changes* and deployment independence; *the provider can deploy whenever they want and the consumer should not need to be redeployed (or restarted when the provider changes)*.

#### Versioning
By introducing a versioned contract package into our consumer we are able to reference the contract in application code, this allows the implementation to change underneath so long as it continues to support the versioned contract. This allows us to update the implementation at will, in a similar way to how webservices are versioned.

#### Deployment independence
In order to gain deployment independence we need to ensure two things, firstly that the plugin can be upgraded at runtime based on an external deployment, and secondly that the upgrade will happen in a predictable time window. In order to achieve this we must make the plugin actively watch a repository and in-place upgrade itself when a change occurs. If the repository cannot be contacted within the deployment window the plugin should stop functioning in order to provide a guarantee that a deployment has successfully completed after that window expires.

#### An example
In the .NET world runtime plugins can be built using AppDomains and a shared folder (as one example).

**Components:**

 - A runtime plugin library
 - A contracts package; built from the provider services' solution, deployed to NuGet
 - The plugin itself; built from the provider services' solution, deployed to a shared folder

**Lifecycle:**

 - Consumer installs the contracts package and runtime plugin library from NuGet
 - Consumer requests a proxy to the contract at runtime from the plugin library
 - Plugin library looks in the shared folder for the current implementation of the plugin, loads it into an isolated app domain and returns a transparent proxy which will call the app-domain
 - Plugin library starts a directory watcher looking for changes in the shared folder
 - When a change occurs the plugin library loads the new implementation into a new AppDomain and updates proxies to point at the new AppDomain
 - Plugin library unloads old AppDomain

#### When to use runtime plugins
