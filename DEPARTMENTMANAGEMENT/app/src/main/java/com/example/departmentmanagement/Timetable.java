package com.example.departmentmanagement;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.GridView;

public class Timetable extends AppCompatActivity {
    GridView gridView;

    static final String[] numbers = new String[] {


            "Aggggggggggggggggggggggggggggghhhhhhhhhhhhhhhhhhhhhhhhhhh", "B", "C", "D", "E",
            "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"

    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_timetable);


    }
}