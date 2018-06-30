var ctx = document.getElementById("myChart").getContext('2d');

draw();

function draw(){
    axios.get('/trends/api/v1/trends')
        .then(handleResponse)
        .then(initChart);

    setTimeout(draw, 10000)
}


function handleResponse(response) {
    return {
        labels: response.data.map(t => t.name),
        scores: response.data.map(t => t.score)
    }
}

function initChart(data) {
    let myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'trends',
                data: data.scores,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgb(204, 201, 96)',
                    'rgb(167, 224, 132)',
                    'rgb(36, 33, 206)',
                    'rgb(135, 226, 211)'
                ]
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
                xAxes: [{
                    ticks: {
                        autoSkip: false
                    }
                }],
            }
        }
    });
}