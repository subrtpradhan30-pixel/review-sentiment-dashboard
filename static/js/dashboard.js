const positiveElement = document.getElementById("positive-count");
const negativeElement = document.getElementById("negative-count");
const neutralElement = document.getElementById("neutral-count");

const positive = Number(positiveElement.textContent);
const negative = Number(negativeElement.textContent);
const neutral = Number(neutralElement.textContent);

const labels = ["Positive", "Negative", "Neutral"];
const data = [positive, negative, neutral];

const chart = new Chart(
    document.getElementById("sentimentChart"),
    {
        type:"pie",
        data:{
            labels:labels,
            datasets:[
                {
                    data:data
                }
            ]
        }
    }
);
const ratingLabels = ["1 Star", "2 Stars", "3 Stars", "4 Stars", "5 Stars"];

const ratingData = [
    ratingCounts[1],
    ratingCounts[2],
    ratingCounts[3],
    ratingCounts[4],
    ratingCounts[5]
];

const ratingChart = new Chart(
    document.getElementById("ratingChart"),
    {
        type: "bar",
        data: {
            labels: ratingLabels,
            datasets: [
                {
                    label: "Reviews",
                    data: ratingData
                }
            ]
        }
    }
);
