const express = require('express');
const app = express();
app.use(express.json());

app.post('/data', (req, res) => {
    console.log('Temperature Data:', req.body.temperature);
    if (req.body.temperature > 50) {
        console.warn('High temperature warning!');
    }
    res.status(200).send('Data received');
});

app.listen(8000, () => {
    console.log('Server is running on port 8000');
});
