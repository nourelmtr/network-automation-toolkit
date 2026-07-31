const table = document.getElementById("deviceTable");

const deviceCount = document.getElementById("deviceCount");
const onlineCount = document.getElementById("onlineCount");
const offlineCount = document.getElementById("offlineCount");
const avgLatency = document.getElementById("avgLatency");

const search = document.getElementById("search");
const lastUpdate = document.getElementById("lastUpdate");

let statusChart = null;
let latencyChart = null;

let allDevices = [];

document
    .getElementById("loadDevices")
    .addEventListener("click", loadDevices);

search.addEventListener("keyup", filterDevices);

loadDevices();

setInterval(loadDevices, 5000);

async function loadDevices() {

    try {

        const response = await fetch("http://127.0.0.1:8000/devices");

        allDevices = await response.json();

        renderTable(allDevices);

        updateStatistics(allDevices);

        updateCharts(allDevices);

        updateTimestamp();

    }

    catch (error) {

        console.error(error);

        alert("Unable to connect to FastAPI.");

    }

}

function renderTable(devices) {

    table.innerHTML = "";

    devices.forEach(device => {

        table.innerHTML += `

        <tr>

            <td>${device.name}</td>

            <td>${device.ip}</td>

            <td>${device.device_type}</td>

            <td>

                <span class="status ${device.reachable ? "online" : "offline"}">

                    ${device.reachable ? "Online" : "Offline"}

                </span>

            </td>

            <td>${device.latency ?? "-"}</td>

        </tr>

        `;

    });

}

function updateStatistics(devices) {

    let online = 0;
    let offline = 0;

    let totalLatency = 0;
    let latencyCount = 0;

    devices.forEach(device => {

        if (device.reachable)
            online++;
        else
            offline++;

        if (device.latency) {

            const latency = parseInt(device.latency);

            if (!isNaN(latency)) {

                totalLatency += latency;
                latencyCount++;

            }

        }

    });

    deviceCount.textContent = devices.length;

    onlineCount.textContent = online;

    offlineCount.textContent = offline;

    avgLatency.textContent =
        latencyCount
            ? Math.round(totalLatency / latencyCount) + " ms"
            : "--";

}

function updateCharts(devices) {

    let online = 0;
    let offline = 0;

    const labels = [];
    const values = [];

    devices.forEach(device => {

        if (device.reachable)
            online++;
        else
            offline++;

        labels.push(device.name);

        values.push(parseInt(device.latency) || 0);

    });

    createStatusChart(online, offline);

    createLatencyChart(labels, values);

}

function filterDevices() {

    const value = search.value.toLowerCase();

    const filtered = allDevices.filter(device =>

        device.name.toLowerCase().includes(value) ||

        device.ip.toLowerCase().includes(value) ||

        device.device_type.toLowerCase().includes(value)

    );

    renderTable(filtered);

    updateStatistics(filtered);

    updateCharts(filtered);

}

function updateTimestamp() {

    const now = new Date();

    lastUpdate.textContent =
        "Last update: " + now.toLocaleTimeString();

}

function createStatusChart(online, offline) {

    if (statusChart)
        statusChart.destroy();

    statusChart = new Chart(

        document.getElementById("statusChart"),

        {

            type: "doughnut",

            data: {

                labels: ["Online", "Offline"],

                datasets: [

                    {

                        data: [online, offline],

                        backgroundColor: [

                            "#22c55e",

                            "#ef4444"

                        ]

                    }

                ]

            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        }

    );

}

function createLatencyChart(labels, values) {

    if (latencyChart)
        latencyChart.destroy();

    latencyChart = new Chart(

        document.getElementById("latencyChart"),

        {

            type: "bar",

            data: {

                labels: labels,

                datasets: [

                    {

                        label: "Latency (ms)",

                        data: values,

                        backgroundColor: "#2563eb"

                    }

                ]

            },

            options: {

                responsive: true,

                scales: {

                    y: {

                        beginAtZero: true

                    }

                }

            }

        }

    );

}