package com.example.infotainment;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.Switch;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {

    DatabaseReference servoRef = FirebaseDatabase.getInstance().getReference().child("servo");
    DatabaseReference canbusRef = FirebaseDatabase.getInstance().getReference().child("canbus");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView gasData = findViewById(R.id.gasValue);
        TextView lightData = findViewById(R.id.lightValue);
        Switch leftLight = (Switch) findViewById(R.id.switchLeftTurn);
        Switch rightLight = (Switch) findViewById(R.id.switchRightTurn);
        Switch brakes = (Switch) findViewById(R.id.switchBrakes);
        Switch parking = (Switch) findViewById(R.id.switchParking);
        EditText servoValue = findViewById(R.id.editTextNumberDecimal);
        Button setServoValue = findViewById(R.id.button);

        ValueEventListener gasListener = new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                Servo sendrecv = snapshot.getValue(Servo.class);
                gasData.setText(String.valueOf(sendrecv.send));
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                // Do nothing?
            }
        };

        ValueEventListener lightListener = new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                CANBus sendrecv = snapshot.getValue(CANBus.class);
                lightData.setText(sendrecv.send);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                // Do nothing?
            }
        };

        servoRef.addValueEventListener(gasListener);
        canbusRef.addValueEventListener(lightListener);

        leftLight.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (b) {
                    canbusRef.child("send").setValue("L");
                }
                else {
                    canbusRef.child("send").setValue("l");
                }
            }
        });

        rightLight.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (b) {
                    canbusRef.child("send").setValue("R");
                }
                else {
                    canbusRef.child("send").setValue("r");
                }
            }
        });

        brakes.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (b) {
                    canbusRef.child("send").setValue("B");
                }
                else {
                    canbusRef.child("send").setValue("b");
                }
            }
        });

        parking.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (b) {
                    canbusRef.child("send").setValue("P");
                }
                else {
                    canbusRef.child("send").setValue("p");
                }
            }
        });

        setServoValue.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (servoValue.getText().length() != 0) {
                    String str = servoValue.getText().toString();
                    int val = Integer.parseInt(str);
                    servoRef.child("send").setValue(val);
                }
            }
        });

    }


}