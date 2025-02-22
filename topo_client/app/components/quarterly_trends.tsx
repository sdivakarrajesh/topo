import React, { useState, useEffect } from 'react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export const formatYAxis = (value) => {
    if (value >= 1000000) {
        return `${(value / 1000000).toFixed(1)}M`; // Convert to millions and round to 1 decimal place
    }
    return value;
};

const QuarterlyRevenueChart = ({ data }) => {
    return (
        <ResponsiveContainer width="100%" height={300}>
            <AreaChart data={data}>
                <CartesianGrid strokeDasharray="4 4" />
                <XAxis dataKey="quarter" />
                <YAxis tickFormatter={formatYAxis}/>
                <Tooltip />
                <Area type="monotone" dataKey="revenue" stroke="#1777ff" fill="#1777ff" fillOpacity={0.8} />
            </AreaChart>
        </ResponsiveContainer>
    );
};

export default QuarterlyRevenueChart;
