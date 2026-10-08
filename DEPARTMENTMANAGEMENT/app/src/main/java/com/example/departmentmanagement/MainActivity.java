package com.example.departmentmanagement;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.Preference;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
EditText e1;
Button b1;
SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        e1 = findViewById(R.id.editTextTextPersonName4);
        b1 = findViewById(R.id.button5);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String a=e1.getText().toString();
                int flg =0;
                if(a.equalsIgnoreCase("")){
                    e1.setError("*");
                    flg++;
                }
                if(flg ==0 ){

                    SharedPreferences.Editor editor = sh.edit();
                    editor.putString("ip",a);
                    editor.putString("url","http://"+a+":8000");
                    editor.apply();
                    Intent ij = new Intent(getApplicationContext(),LOGIN.class);
                    startActivity(ij);


                }
            }
        });
    }
}