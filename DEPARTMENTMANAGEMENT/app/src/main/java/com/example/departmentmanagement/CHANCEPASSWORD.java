package com.example.departmentmanagement;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class CHANCEPASSWORD extends AppCompatActivity {
    EditText e1;
    EditText e2;
    EditText e3;
    Button b1;
    SharedPreferences sh;

    String url = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chancepassword);
        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        url = sh.getString("url", "") + "/andchangepass";
        e1 = findViewById(R.id.editTextTextPersonName6);
        e2 = findViewById(R.id.editTextTextPersonName9);
        e3 = findViewById(R.id.editTextTextPersonName10);
        b1 = findViewById(R.id.button2);
        b1.setOnClickListener(new View.OnClickListener() {
                                  @Override
                                  public void onClick(View view) {
                                      String a = e1.getText().toString();
                                      String b = e2.getText().toString();
                                      String c = e3.getText().toString();
                                      int flg = 0;
                                      if (a.equalsIgnoreCase("")) {
                                          e1.setError("*");
                                          flg++;
                                      }
                                      if (b.equalsIgnoreCase("")) {
                                          e2.setError("*");
                                          flg++;
                                      }
                                      if (c.equalsIgnoreCase("")) {
                                          e3.setError("*");
                                          flg++;
                                      }


                                      if (flg == 0) {

                                          RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
                                          StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                                                  new Response.Listener<String>() {
                                                      @Override
                                                      public void onResponse(String response) {
                                                          //  Toast.makeText(getApplicationContext(), response, Toast.LENGTH_LONG).show();

                                                          // response
                                                          try {
                                                              JSONObject jsonObj = new JSONObject(response);
                                                              if (jsonObj.getString("status").equalsIgnoreCase("ok")) {


                                                                  Toast.makeText(CHANCEPASSWORD.this, "password changed successfully", Toast.LENGTH_SHORT).show();
                                                                  Intent in = new Intent(getApplicationContext(), MainActivity2.class);
                                                                  startActivity(in);

                                                              }


                                                              // }
                                                              else {
                                                                  Toast.makeText(getApplicationContext(), "Not found", Toast.LENGTH_LONG).show();
                                                              }

                                                          } catch (Exception e) {
                                                              Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                                                          }
                                                      }
                                                  },
                                                  new Response.ErrorListener() {
                                                      @Override
                                                      public void onErrorResponse(VolleyError error) {
                                                          // error
                                                          Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                                                      }
                                                  }
                                          ) {
                                              @Override
                                              protected Map<String, String> getParams() {
                                                  SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                                                  Map<String, String> params = new HashMap<String, String>();
                                                  params.put("a", a);
                                                  params.put("b", b);
                                                  params.put("c", c);
                                                  String id=sh.getString("uid","");
                                                  params.put("uid",id);
                                                  return params;
                                              }
                                          };

                                          int MY_SOCKET_TIMEOUT_MS = 100000;

                                          postRequest.setRetryPolicy(new DefaultRetryPolicy(
                                                  MY_SOCKET_TIMEOUT_MS,
                                                  DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                                                  DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
                                          requestQueue.add(postRequest);

                                      }
                                  }
                              }
        );
    }
}