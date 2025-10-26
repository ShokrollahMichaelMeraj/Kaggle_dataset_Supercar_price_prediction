"use strict";
/* Car.js
 * Description: Defines the Car class and sub-classes
 * Date: 25 Oct 2025
 */
class Car {
    constructor(carName, year, region, condition, displacement, horsepower, torque, weight, topSpeed, acceleration, fuel, drivetrain, transmission) {
        this.m_id = Car.carIDMaker;
        this.m_carName = carName;
        this.m_year = year;
        this.m_region = region;
        this.m_condition = condition;
        this.m_displacement = displacement;
        this.m_horsepower = horsepower;
        this.m_torque = torque;
        this.m_weight = weight;
        this.m_topSpeed = topSpeed;
        this.m_acceleration = acceleration;
        this.m_fuel = fuel;
        this.m_drivetrain = drivetrain;
        this.m_transmission = transmission;
        Car.carIDMaker++;
    }
}
Car.carIDMaker = 0;
