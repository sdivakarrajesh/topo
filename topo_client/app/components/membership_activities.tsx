import React from 'react';
import { Table } from 'antd';

const MembershipsActivitiesTable = ({ data }) => {
    // Define table columns with sorting and filtering
    const membershipTypes = [...new Set(data.map(item => item.membership_type))];
    const activityTypes = [...new Set(data.map(item => item.activity_type))];

    const columns = [
        {
            title: 'Membership Type',
            dataIndex: 'membership_type',
            sorter: (a, b) => a.membership_type.localeCompare(b.membership_type),
            filters: membershipTypes.map(type => ({ text: type, value: type })),
            onFilter: (value, record) => record.membership_type === value,
        },
        {
            title: 'Activity',
            dataIndex: 'activity_type',
            sorter: (a, b) => a.activity_type.localeCompare(b.activity_type),
            filters: activityTypes.map(type => ({ text: type, value: type })),
            onFilter: (value, record) => record.activity_type === value,
        },
        {
            title: 'Revenue',
            dataIndex: 'revenue',
            sorter: (a, b) => a.revenue - b.revenue,
            render: (text) => `$${text.toFixed(2)}`,  // Format the revenue as currency
        },
        {
            title: 'Duration (min)',
            dataIndex: 'duration_minutes',
            sorter: (a, b) => a.duration_minutes - b.duration_minutes,
        },
    ];

    return (
        <Table
            //@ts-ignore
            columns={columns}
            dataSource={data}
            rowKey="id"
            pagination={{ pageSize: 10 }}
            scroll={{ x: 'max-content' }}
        />
    );
};

export default MembershipsActivitiesTable;
