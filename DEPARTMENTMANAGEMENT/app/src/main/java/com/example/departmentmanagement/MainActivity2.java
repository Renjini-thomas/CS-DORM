package com.example.departmentmanagement;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.MenuItem;
import android.view.View;
import android.view.Menu;

import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.navigation.NavigationView;

import androidx.annotation.NonNull;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.appcompat.app.AppCompatActivity;

import com.example.departmentmanagement.databinding.ActivityMain2Binding;

public class MainActivity2 extends AppCompatActivity {

    private AppBarConfiguration mAppBarConfiguration;
    private ActivityMain2Binding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMain2Binding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        setSupportActionBar(binding.appBarMain.toolbar);
       // binding.appBarMain.fab.setOnClickListener(new View.OnClickListener() {
         //   @Override
           // public void onClick(View view) {
             //   Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
              //          .setAction("Action", null).show();
            //}
        //});
        DrawerLayout drawer = binding.drawerLayout;
        NavigationView navigationView = binding.navView;
        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        mAppBarConfiguration = new AppBarConfiguration.Builder(
                R.id.nav_home, R.id.nav_gallery, R.id.nav_slideshow)
                .setOpenableLayout(drawer)
                .build();
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_content_main);
        NavigationUI.setupActionBarWithNavController(this, navController, mAppBarConfiguration);
        NavigationUI.setupWithNavController(navigationView, navController);
        navigationView.setItemIconTintList(null);
        navigationView.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                int id = item.getItemId();
                if(id == R.id.nav_home){
                    Intent ij = new Intent(getApplicationContext(),MainActivity2.class);
                    startActivity(ij);
                }

                if(id == R.id.nav_gallery){
                    Intent ij = new Intent(getApplicationContext(),VIEWPROFILE.class);
                    startActivity(ij);
                }
                if(id == R.id.nav_slideshow){
                    Intent ij = new Intent(getApplicationContext(),VIEWEVENT.class);
                    startActivity(ij);
                }
                if(id == R.id.nav_NOTI){
                    Intent ij = new Intent(getApplicationContext(),VIEWNOTIFICATION.class);
                    startActivity(ij);
                }
                if(id == R.id.nav_COMPLAINT){
                    Intent ij = new Intent(getApplicationContext(),SENDCOMPLAINTSANDREPLY.class);
                    startActivity(ij);
                }
                if(id == R.id.nav_TIMETABLE){
                    SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    if(sh.getString("d","").equalsIgnoreCase("MONDAY")) {
                        Intent ij = new Intent(getApplicationContext(), monday.class);
                        startActivity(ij);
                    }
                    if(sh.getString("d","").equalsIgnoreCase("TUESDAY")) {
                        Intent ik = new Intent(getApplicationContext(), tuesday.class);
                        startActivity(ik);
                    }
                    if(sh.getString("d","").equalsIgnoreCase("WEDNESDAY")) {
                        Intent il = new Intent(getApplicationContext(), wednesday.class);
                        startActivity(il);
                    }
                    if(sh.getString("d","").equalsIgnoreCase("THURSDAY")) {
                        Intent im = new Intent(getApplicationContext(), thursday.class);
                        startActivity(im);
                    }
                    if(sh.getString("d","").equalsIgnoreCase("FRIDAY")) {
                        Intent in = new Intent(getApplicationContext(), friday.class);
                        startActivity(in);
                    }

                }
                if(id == R.id.nav_CHPASS){
                    Intent ij = new Intent(getApplicationContext(),CHANCEPASSWORD.class);
                    startActivity(ij);
                }
                if(id == R.id.nav_LOG){
                    Intent ij = new Intent(getApplicationContext(),LOGIN.class);
                    startActivity(ij);
                }
                return true;
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main_activity2, menu);
        return true;
    }

    @Override
    public boolean onSupportNavigateUp() {
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_content_main);
        return NavigationUI.navigateUp(navController, mAppBarConfiguration)
                || super.onSupportNavigateUp();
    }
}