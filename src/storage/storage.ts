
export interface Event {
    type: 'charge' | 'discharge';
    amount: number;
    timestamp: Date;
}

export const battery = {
    charge: 0,
    maxCapacity: 20,
    lastUpdated: new Date()
};

export const history = {
    events: [] as Event[]
}