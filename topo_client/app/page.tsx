"use client";
import Image from "next/image";
import styles from "./page.module.scss";
import axios from 'axios';
import RevenueBreakdownChart from "./components/revenue_chart";
import QuarterlyRevenueChart from "./components/quarterly_trends";
import MembershipsActivitiesTable from "./components/membership_activities";
import { useEffect, useState } from "react";
import ss1 from '../../data/ss1.png';

export default function Home() {
  const [revenueData, setRevenueData] = useState([]);
  const [quarterlyRevenueData, setQuarterlyRevenueData] = useState([]);
  const [activityData, setActivityData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8989/api/data/?format=json');
        const data = response.data;

        // Process the data for Revenue Breakdown Chart
        const breakdownData = data.revenue_breakdowns.map(item => ({
          activity_type: item.activity_type,
          percentage: item.percentage
        }));
        console.log("breakdownData", breakdownData);
        setRevenueData(breakdownData);

        // Process the data for Quarterly Revenue Chart
        const quarterlyData = data.quarterly_reports
        .filter(qr => qr.report_type === "FitPro: Annual Summary 2023")
        .map(item => ({
          quarter: item.quarter,
          revenue: parseFloat(item.revenue)
        }));
        console.log("quarterlyData", quarterlyData);
        setQuarterlyRevenueData(quarterlyData);

        // Process the data for Memberships & Activities Table
        const activityTableData = data.activity_sessions.map(session => ({
          membership_type: session.membership.membership_type,
          activity_type: session.activity_type,
          revenue: parseFloat(session.revenue),
          duration_minutes: session.duration_minutes
        }));
        console.log("activityTableData", activityTableData);
        setActivityData(activityTableData);

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);
  return (
    <div>
      <center>
        <h1>Topo Analytics</h1>
        <Image src={ss1} alt="Screenshot" width={500} height={300} />
      </center>
      <br /><br />
      <div className={styles.charts}>
        <div className={styles.chart}>
          <h3 className={styles.h3}>Revenue Breakdown by Activity</h3>
          <RevenueBreakdownChart data={revenueData} />
        </div>

        <div className={styles.chart}>
          <h3 className={styles.h3}>Quarterly Revenue Trends</h3>
          <QuarterlyRevenueChart data={quarterlyRevenueData} />
        </div>
      </div>
      <br /> <br />
      <div>
        <h3 className={styles.h3}>Memberships & Activities Breakdown</h3>
        <MembershipsActivitiesTable data={activityData} />
      </div>
    </div>
  );
}
