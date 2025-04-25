import {Request, Response} from 'express';
import {battery} from '../storage/batteryStorage';

export const getStatus = (_: Request, res: Response) => {
    const {charge, maxCapacity, lastUpdated} = battery;
    res.json({
        chargePercent: (charge/maxCapacity) * 100,
        maxCapacity,
        lastUpdated,
    });
};

export const chargeBattery = (req: Request, res: Response) => {
    const {amount} = req.body;
    if (typeof amount !== 'number' || amount <= 0) {
        res.status(400).json({error: 'Invalid charge amount'});
    }
    if (battery.charge + amount > battery.maxCapacity) {
        res.status(400).json({error: 'Exceeds max capacity'});
    } 
    else {
        battery.charge += amount;
        battery.lastUpdated = new Date();
        battery.history.unshift({type: 'charge', amount, timestamp: new Date()});
        battery.history = battery.history.slice(0, 20);
        res.status(200).json({message: "Battery charged successfully", newCharge: battery.charge});
    }
};

export const dischargeBattery = (req: Request, res: Response) => {
    const {amount} = req.body;
    if (typeof amount !== 'number' || amount <= 0) {
        res.status(400).json({error: 'Invalid discharge amount'});
    }
    if (battery.charge < amount) {
        res.status(400).json({error: 'Insufficient battery charge'});
    }
    else{
        battery.charge -= amount;
        battery.lastUpdated = new Date();
        battery.history.push({type: 'discharge', amount, timestamp: new Date()});
        res.json({message: "Battery discharged successfully", newCharge: battery.charge});
    }
};

export const getHistory = (req: Request, res: Response) => {
    res.json(battery.history);
};