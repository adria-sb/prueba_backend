import { Router } from 'express';
import * as controller from '../controllers/battery.controller';

const router = Router();

router.get('/status', controller.getStatus);
router.post('/charge', controller.chargeBattery);
router.post('/discharge', controller.dischargeBattery);
router.get('/history', controller.getHistory);

export default router;