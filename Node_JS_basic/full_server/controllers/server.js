// full_server/server.js

const express = require('express');
const routes = require('./routes');

const app = express();
const PORT = 1245;

app.use(routes);

app.listen(PORT, () => {
  console.log('Server listening on port ' + PORT);
});

export default app;
