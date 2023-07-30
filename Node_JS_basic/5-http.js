const http = require('http');
const countStudents = require('./3-read_file_async');

// Set the hostname and port for the server
const hostname = '127.0.0.1';
const port = 1245;

// Get the database filename from the command line arguments
const DB = process.argv[2];

// Create the HTTP server
const app = http.createServer((req, res) => {
  // Set the status code and response header for all requests
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  // Check the URL path to determine the response
  if (req.url === '/') {
    // Handle the root route '/'
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    // Handle the '/students' route
    res.write('This is the list of our students\n');
    // Call the countStudents function asynchronously
    countStudents(DB).then((result) => {
      // Handle the successful result by sending the data as the response
      res.end(result.join('\n'));
    }).catch((error) => {
      // Handle any errors that occur during the countStudents function
      // by sending the error message as the response
      res.end(`${error.message}`);
    });
  } else {
    // Handle other routes with a 404 Not Found response
    res.statusCode = 404;
    res.end('Not Found');
  }
});

// Start the server and listen on the specified port and hostname
app.listen(port, hostname);

// Export the app variable to be used in other files
module.exports = app;
