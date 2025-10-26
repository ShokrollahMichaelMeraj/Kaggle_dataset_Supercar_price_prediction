"use strict";
/* CarServices.js
 * Description: Defines the services/functionality for the Car class
 * Date: 25 Oct 2025
 */
class CarController {
    constructor() {
        this.carsArr = [];
    }
    add(carToAdd) {
        this.carsArr.push(carToAdd);
        localStorage.LocalCarArray = JSON.stringify(this.carsArr);
    }
    getAll() {
        return JSON.parse(localStorage.LocalCarArray);
    }
    deleteCar(id) {
        this.carsArr.filter((carToDelete) => {
            // if true we keep the car in the array, if false, we filter it out
            return carToDelete.m_id != id;
        });
        localStorage.LocalCarArray = JSON.stringify(this.carsArr);
    }
}
