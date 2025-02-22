import { formatYAxis } from '../app/components/quarterly_trends'; // Import the helper function if it's separated

describe('formatYAxis', () => {
    it('should format values greater than or equal to 1 million as M', () => {
        expect(formatYAxis(1000000)).toBe('1.0M');
        expect(formatYAxis(2500000)).toBe('2.5M');
    });

    it('should return the value as is if less than 1 million', () => {
        expect(formatYAxis(500000)).toBe(500000);
        expect(formatYAxis(0)).toBe(0);
    });
});
