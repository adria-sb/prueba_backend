import express from 'express';
import batteryRoutes from './routes/battery.routes';
import { errorHandler } from './middleware/errorHandler';


const app = express();
const PORT = 3000;

app.use(express.json());
app.use('/api/battery', batteryRoutes, errorHandler);

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

