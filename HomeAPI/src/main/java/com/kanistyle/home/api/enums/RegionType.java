package com.kanistyle.home.api.enums;

public enum RegionType {

    LIVING_ROOM("LIVING_ROOM");

    private final String value;

    RegionType(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }

}
