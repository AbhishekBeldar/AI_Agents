
const travelForm = document.getElementById("travelForm");
const planButton = document.getElementById("planButton");
const statusMessage = document.getElementById("status");
const resultSection = document.getElementById("result");

travelForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const destination = document.getElementById("destination").value;
    const days = Number(document.getElementById("days").value);
    const people = Number(document.getElementById("people").value);

    if (!destination) {
        showStatus("Please select a destination.", true);
        return;
    }

    if (!Number.isInteger(days) || days < 1 || days > 30) {
        showStatus("Days must be between 1 and 30.", true);
        return;
    }

    if (!Number.isInteger(people) || people < 1 || people > 20) {
        showStatus("People must be between 1 and 20.", true);
        return;
    }

    planButton.disabled = true;
    planButton.textContent = "Creating your plan...";
    showStatus("Please wait while we prepare your trip.", false);
    resultSection.hidden = true;

    try {
        const response = await fetch("/api/plan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                destination: destination,
                days: days,
                people: people
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Unable to create your travel plan.");
        }

        displayPlan(data);
        showStatus("Your travel plan is ready!", false);
        resultSection.hidden = false;
    } catch (error) {
        showStatus(
            error.message || "Could not connect to the server. Check that the backend is running.",
            true
        );
    } finally {
        planButton.disabled = false;
        planButton.textContent = "Generate Travel Plan";
    }
});

function displayPlan(plan) {
    document.getElementById("resultDestination").textContent =
        plan.destination;

    document.getElementById("resultDays").textContent =
        `${plan.days} day(s)`;

    document.getElementById("resultPeople").textContent =
        `${plan.people} person(s)`;

    document.getElementById("resultBudget").textContent =
        Number(plan.estimated_budget).toLocaleString("en-IN", {
            style: "currency",
            currency: "INR",
            maximumFractionDigits: 0
        });

    document.getElementById("resultWeather").textContent =
        plan.weather;

    const placesList = document.getElementById("resultPlaces");
    placesList.replaceChildren();

    if (Array.isArray(plan.places) && plan.places.length > 0) {
        plan.places.forEach(function (place) {
            const listItem = document.createElement("li");
            listItem.textContent = place;
            placesList.appendChild(listItem);
        });
    } else {
        const listItem = document.createElement("li");
        listItem.textContent = "No places found.";
        placesList.appendChild(listItem);
    }
}

function showStatus(message, isError) {
    statusMessage.textContent = message;
    statusMessage.className = isError ? "status error" : "status success";
}
