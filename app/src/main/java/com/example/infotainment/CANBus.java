package com.example.infotainment;

import com.google.firebase.database.IgnoreExtraProperties;

@IgnoreExtraProperties
public class CANBus {

    public String send;
    public int recv;

    public CANBus() {

    }

    public CANBus(String send, int recv) {
        this.send = send;
        this.recv = recv;
    }

    public String getSend() {
        return send;
    }

    public int getRecv() {
        return recv;
    }
}
