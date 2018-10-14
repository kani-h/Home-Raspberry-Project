package com.kanistyle.home.api.entity;

import com.kanistyle.home.api.enums.RegionType;
import org.hibernate.annotations.CreationTimestamp;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name = "hygrothermograph")
public class Hygrothermograph {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    Integer id;

    @Enumerated(EnumType.STRING)
    @Column(name = "region")
    RegionType region;

    @Column(name = "temperature")
    Double temperature;

    @Column(name = "humidity")
    Double humidity;

    @Column(name = "measurement_date")
    @CreationTimestamp
    @Temporal(TemporalType.TIMESTAMP)
    Date measurementDate;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public RegionType getRegion() {
        return region;
    }

    public void setRegion(RegionType region) {
        this.region = region;
    }

    public Double getTemperature() {
        return temperature;
    }

    public void setTemperature(Double temperature) {
        this.temperature = temperature;
    }

    public Double getHumidity() {
        return humidity;
    }

    public void setHumidity(Double humidity) {
        this.humidity = humidity;
    }

    public Date getMeasurementDate() {
        return measurementDate;
    }

    public void setMeasurementDate(Date measurementDate) {
        this.measurementDate = measurementDate;
    }
}
