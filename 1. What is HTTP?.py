1. What is HTTP? 
HTTP stands for Hyper Text Transfer Protocol. It is a set of 
instructions which outline a format by which data (or files)
can be transported from server to client. 

2. What is URL? 
 URL stands for Uniform Resource Locator. It is a unique identifier used
 to locate a resource on the internet. 

 3. What is DNS? 
 DNS stands for Domain Name System. Basically, it takes the URL 
 and translates it into an IP address. 

 4. What is a query string? 
  A query string is a portion of the URL where data is passed to 
  a web application. It is in the format of key-value pairs. 

 5.  List 2 HTTP Verbs and their use cases: 
    GET - Requests to specified server certain data or resources. example: search forms.
    POST - Requests that a web server will accept data enclosed in 
    body of the request message. example: uploading a file. 

 6. What is an Http Request? 
    An HTTP request is made by a client to a host with the aim of
    requesting access to information on that server. 

 7. What is an HTTP response? 
    An HTTP response is a response from the server which informs
    the client that the request has been carried out or that an 
    error has occured. Ideally, it provides the client with
    the material requested. example: response from Weatherchannel.com 
    would be weather in my local area (if that was what was requested).

 8. What is an HTTP header? 
   A request header is one type of HTML header. It can be used to provide
   information about the context of the request, and allows the
   server to tailor its response. 
   For example, the Accept headers indicate the allowable methods of
   server response. 
   The HTTP host header is a request header which specifies a 
   domain which the client would like to access. 

   Response headers are another type of HTML header. They are used to give a more detailed context of the response.  Server and Age would be two examples. Server describes the origin software that handled the request. Age contains the time in which the object was in a proxy cache. 

   9. What happens when you type a URL into a browser? 
    1. browser uses DNS to convert the URL to IP address. 
    2. Browser makes request to IP address
    3. Browser sends its response. 
    4. Browser makes a DOM from the given HTML
    5. Browser makes seperate IP requests to the server for 
    additional content such as images, css, etc. 

 10. Using curl, make a GET request to the icanhazdadjoke.com API to find all jokes involving the word “pirate”
   curl https://icanhazdadjoke.com/search\?term\=pirate

 11. Use dig to find what the IP address is for icanhazdadjoke.com
     dig icanhazdadjoke.com (+ short)

 12. Make a simple web page and serve it using python3 -m http.server. Visit the page in a browser.
 alludwig@als-MacBook-Air ConnectFour % ls
connect4.html				connect4solution.js
connect4indexfinishedproduct.html	connect4stylesfinishedproduct.css
connect4mainfinishedproduct.js		connectfourmain.js
connect4problem.css			connectfourmainredo.js
connect4problem.js			connnectfourstyles.css
connect4revisit.js			indexproblem.html
connect4solution.css			indexsolution.html
alludwig@als-MacBook-Air ConnectFour % python3 -m http.server
Serving HTTP on :: port 8000 (http://[::]:8000/) 













