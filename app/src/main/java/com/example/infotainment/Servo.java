package com.example.infotainment;

import com.google.firebase.database.IgnoreExtraProperties;

@IgnoreExtraProperties
public class Servo {

    public int send;
    public int recv;

    public Servo() {

    }

    public Servo(int send, int recv) {
        this.send = send;
        this.recv = recv;
    }

    public int getSend() {
        return send;
    }

    public int getRecv() {
        return recv;
    }
}
