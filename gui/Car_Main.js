"use strict";
/* Car_Main.js
 * Description: Defines the functionality for the App's main page
 * Date: 25 Oct 2025
 */
var _a;
// MODALS ----------
let container = document.getElementById("container");
let openModalButtons = document.querySelectorAll("[data-modal-target]");
let closeModalButtons = document.querySelectorAll("[data-close-button]");
let overlay = document.getElementById("overlay");
container.addEventListener("click", function (e) {
    if (e.target && e.target instanceof HTMLElement) {
        if (e.target.classList.contains("open-modal-button")) {
            // sending index information 
            let modal = document.querySelector(String(e.target.dataset.modalTarget));
            if (e.target.classList.contains("delete-button") || e.target.classList.contains("info-button")) {
                modal.dataset.index = e.target.dataset.index;
                modal.dataset.rowBtnID = e.target.id;
            }
            // Create More Info Table
            if (e.target.classList.contains("info-button")) {
                let carArray = carCtlr.getAll();
                let carOfInterest = carArray[Number(e.target.dataset.index)];
                let infoTable = document.getElementById("more-info-table");
                infoTable.innerHTML = "";
                for (let [item, val] of Object.entries(carOfInterest)) {
                    let infoRow = document.createElement("tr");
                    let key = document.createElement("td");
                    let value = document.createElement("td");
                    if (carOfInterest.hasOwnProperty(item)) {
                        key.innerHTML = item.slice(2);
                        value.innerHTML = String(val);
                    }
                    infoRow.append(key, value);
                    infoTable.append(infoRow);
                }
            }
            openModal(modal);
        }
    }
});
overlay === null || overlay === void 0 ? void 0 : overlay.addEventListener("click", () => {
    const modals = document.querySelectorAll(".modal.active");
    modals.forEach(modal => {
        closeModal(modal);
    });
});
closeModalButtons.forEach(button => {
    button.addEventListener("click", () => {
        const modal = button.closest(".modal");
        closeModal(modal);
    });
});
function openModal(modal) {
    if (modal == null)
        return;
    if (overlay == null)
        return;
    modal.classList.add("active");
    overlay.classList.add("active");
}
function closeModal(modal) {
    if (modal == null)
        return;
    if (overlay == null)
        return;
    modal.classList.remove("active");
    overlay.classList.remove("active");
}

// ADDING A NEW CAR ----------
// create an instance of the class, save object to local memory
// create a <tr> with <td>'s name, price, more info, delete for the main page table
let carCtlr = new CarController();
const carTable = document.getElementById("car-table-body");
const carForm = document.getElementById("new-car-form");
const addCarModal = document.getElementById("add-car-modal");
(_a = document.getElementById("create-car-button")) === null || _a === void 0 ? void 0 : _a.addEventListener("click", () => {
    let newCarName = document.getElementById("name-input");
    let newCarYear = document.getElementById("year-input");
    let newCarRegion = document.getElementById("region-input");
    let newCarCondition = document.getElementById("condition-input");
    let newCarDisplacement = document.getElementById("displacement-input");
    let newCarHorsepower = document.getElementById("horsepower-input");
    let newCarTorque = document.getElementById("torque-input");
    let newCarWeight = document.getElementById("weight-input");
    let newCarTopSpeed = document.getElementById("top-speed-input");
    let newCarAcceleration = document.getElementById("acceleration-input");
    /* let newCarFuel = document.getElementById("fuel-input");
    let newCarDrivetrain = document.getElementById("drivetrain-input");
    let newCarTransmission = document.getElementById("transmission-input"); */

    let newCarID = "";
    const newTableRow = document.createElement("tr");
    let predictionCell = document.createElement("td");
    let completeForm = true;
    let errorBox = document.getElementById("error-message-box");

    let newCar = new Car(newCarName.value, Number(newCarYear.value), newCarRegion.value, newCarCondition.value, Number(newCarDisplacement.value), Number(newCarHorsepower.value), Number(newCarTorque.value), Number(newCarWeight.value), Number(newCarTopSpeed.value), Number(newCarAcceleration.value));
    predictionCell.innerHTML = newCar.m_displacement;
    carCtlr.add(newCar);
    newCarID = String(newCar.m_id);

    // validation code for required input fields
    if (newCarName.value == "") {
        errorBox.innerHTML = "***Please enter a name***";
        completeForm = false;
    }
    if (newCarYear.value == "") {
        errorBox.innerHTML = "***Please enter a year***";
        completeForm = false;
    }
    if (newCarRegion.value == "") {
        errorBox.innerHTML = "***Please enter a region***";
        completeForm = false;
    }
    if (newCarCondition.value == "") {
        errorBox.innerHTML = "***Please enter a condition***";
        completeForm = false;
    }
    if (newCarDisplacement.value == "") {
        errorBox.innerHTML = "***Please enter a displacement***";
        completeForm = false;
    }
    if (newCarHorsepower.value == "") {
        errorBox.innerHTML = "***Please enter a horsepower***";
        completeForm = false;
    }
    if (newCarTorque.value == "") {
        errorBox.innerHTML = "***Please enter a torque***";
        completeForm = false;
    }
    if (newCarWeight.value == "") {
        errorBox.innerHTML = "***Please enter a weight***";
        completeForm = false;
    }
    if (newCarTopSpeed.value == "") {
        errorBox.innerHTML = "***Please enter a top speed***";
        completeForm = false;
    }
    if (newCarAcceleration.value == "") {
        errorBox.innerHTML = "***Please enter an acceleration***";
        completeForm = false;
    }
/*     if (newCarFuel.value == "") {
        errorBox.innerHTML = "***Please enter a fuel type***";
        completeForm = false;
    }
    if (newCarDrivetrain.value == "") {
        errorBox.innerHTML = "***Please enter a drivetrain***";
        completeForm = false;
    }
    if (newCarTransmission.value == "") {
        errorBox.innerHTML = "***Please enter a transmission***";
        completeForm = false;
    } */

    // ADD INFO TO MAIN TABLE ----------
    if (completeForm) {
        // Car Name
        let nameCell = document.createElement("td");
        nameCell.setAttribute("class", "name-cell");
        nameCell.innerHTML = newCarName.value;

        // Price Prediction Output
        predictionCell.setAttribute("class", "prediction-cell");

        // More Info
        let moreInfoCell = document.createElement("td");
        let moreInfoButton = document.createElement("button");
        moreInfoButton.setAttribute("class", "info-button");
        moreInfoButton.classList.add("open-modal-button");
        moreInfoButton.setAttribute("id", "info-button-" + newCarID);
        moreInfoButton.dataset.modalTarget = "#more-info-modal";
        moreInfoButton.dataset.index = newCarID;
        moreInfoButton.innerHTML = "more info";

        // Delete
        let deleteCell = document.createElement("td");
        let deleteButton = document.createElement("button");
        deleteButton.setAttribute("class", "delete-button");
        deleteButton.classList.add("open-modal-button");
        deleteButton.setAttribute("id", "delete-button-" + newCarID);
        deleteButton.dataset.modalTarget = "#confirm-delete";
        deleteButton.dataset.index = newCarID;
        deleteButton.innerHTML = "delete";
        moreInfoCell.append(moreInfoButton);
        deleteCell.append(deleteButton);

        // Make Table Row
        newTableRow.append(nameCell, predictionCell, moreInfoCell, deleteCell);
        carTable.append(newTableRow);
        carForm.reset();
        /* let specificFields = document.querySelectorAll(".category-specific");
        specificFields.forEach(field => { field.classList.remove("active"); }); */
        errorBox.innerHTML = "";
        closeModal(addCarModal);
        // sort the rows
        const allRows = Array.from(carTable.querySelectorAll("tr"));
        while (carTable.firstChild) {
            carTable.removeChild(carTable.firstChild);
        }
        carTable.append(...allRows);
    }
});
// DELETE BUTTONS ----------
let finalDeleteButton = document.getElementById("final-delete-button");
finalDeleteButton.addEventListener("click", function () {
    let modal = finalDeleteButton.closest(".modal");
    carCtlr.deleteCar(Number(modal.dataset.index));
    let tableRowBtn = document.getElementById(String(modal.dataset.rowBtnID));
    let tableRow = tableRowBtn.closest("tr");
    tableRow.remove();
    closeModal(modal);
});
