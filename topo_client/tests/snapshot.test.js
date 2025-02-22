import { render } from '@testing-library/react';
import QuarterlyRevenueChart from '../app/components/quarterly_trends'; // Import the helper function if it's separated

describe('QuarterlyRevenueChart Snapshot', () => {
    const mockData = [
        { quarter: 'Q1', revenue: 2000000 },
        { quarter: 'Q2', revenue: 2500000 },
    ];

    it('should match the snapshot', () => {
        const { asFragment } = render(<QuarterlyRevenueChart data={mockData} />);
        expect(asFragment()).toMatchSnapshot(); // This will store a snapshot of the rendered component
    });
});
