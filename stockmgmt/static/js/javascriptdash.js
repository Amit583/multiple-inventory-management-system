document.addEventListener("DOMContentLoaded", function () {
    console.log("Dashboard Loaded! Fetching data...");

    // Ensure Chart.js Plugin is Registered
    Chart.register(ChartDataLabels);

    // Function to Calculate Total (for Pie Chart)
    function calculateTotal(data) {
        return data.reduce((acc, value) => acc + value, 0);
    }

    // Get Chart Elements
    const barCtx = document.getElementById("barChart").getContext("2d");
    const pieCtx = document.getElementById("pieChart").getContext("2d");

    let barChart, pieChart; // Declare charts globally

    // Function to Fetch & Update Charts
    function updateCharts() {
        fetch("/chart_data/")  
            .then(response => response.json())
            .then(data => {
                console.log("Chart Data Received:", data);

                // Destroy Existing Charts Before Creating New Ones
                if (barChart) barChart.destroy();
                if (pieChart) pieChart.destroy();

                //  Calculate Maximum Value for Scaling
                let maxDataValue = Math.max(...data.bar_chart.datasets.flatMap(dataset => dataset.data));
                let yMax = maxDataValue * 1.3; // Apply the 1.3 multiplier

                //  Create Bar Chart
                barChart = new Chart(barCtx, {
                    type: "bar",
                    data: {
                        labels: data.labels,
                        datasets: data.bar_chart.datasets.map((dataset, index) => ({
                            label: dataset.label,
                            data: dataset.data,
                            backgroundColor: ["#ffbd33", "#75ff33", "#ff5733", "#113c9d", "#335cff"][index % 5], // Cycle Colors
                            borderColor: "#fff",
                            borderWidth: 3,
                            hoverBorderWidth: 4,
                        })),
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: yMax,  //  APPLYING THE MULTIPLIER
                                ticks: { color: "#222", font: { size: 14 } },
                            },
                            x: { ticks: { color: "#222", font: { size: 14 } } },
                        },
                        plugins: {
                            legend: { labels: { color: "#222", font: { size: 16 } } },
                            datalabels: { anchor: "end", align: "top", color: "#000", font: { size: 14, weight: "bold" } },
                        },
                    },
                });

                // Create Pie Chart
                pieChart = new Chart(pieCtx, {
                    type: "doughnut",
                    data: {
                        labels: data.pie_chart.labels,
                        datasets: [{
                            label: "Total Count",
                            data: data.pie_chart.data,
                            backgroundColor: ["#ff5733", "#ffbd33", "#75ff33", "#113c9d", "#335cff"],
                            borderColor: "#fff",
                            borderWidth: 3,
                            hoverOffset: 15,
                        }],
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        animation: {  
                            animateScale: true,  
                            animateRotate: true, 
                            duration: 1200,      
                            easing: 'easeOutBounce',
                        },
                        plugins: {
                            legend: { labels: { color: "#222", font: { size: 16 } } },
                            tooltip: {
                                enabled: true,
                                callbacks: {
                                    label: function (context) {
                                        const total = calculateTotal(context.dataset.data);
                                        const percentage = ((context.raw / total) * 100).toFixed(2);
                                        return `${context.label}: ${context.raw} (${percentage}%)`;
                                    },
                                },
                            },
                            datalabels: {
                                color: "#fff",
                                font: { size: 14, weight: "bold" },
                                formatter: (value, context) => {
                                    const total = calculateTotal(context.dataset.data);
                                    const percentage = ((value / total) * 100).toFixed(1);
                                    return `${value} (${percentage}%)`;
                                },
                            },
                        },
                    },
                });
            })
            .catch(error => console.error("Error fetching chart data:", error));
    }

    // Load Charts Initially
    updateCharts();

    // Set Interval to Refresh Every 30s
    setInterval(updateCharts, 30000);
});
