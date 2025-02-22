import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const formatYAxis = (value) => {
    return `${value}%`;
}

const RevenueBreakdownChart = ({ data }) => {
    return (
        <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="activity_type" />
                <YAxis tickFormatter={formatYAxis} />
                <Tooltip />
                <Bar dataKey="percentage" fill="#B7B1F2" />
            </BarChart>
        </ResponsiveContainer>
    );
};

export default RevenueBreakdownChart;
