package com.example.departmentmanagement;

import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;

import com.google.android.material.bottomnavigation.BottomNavigationView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.example.departmentmanagement.databinding.ActivityMoreinfoBinding;

public class Moreinfo extends AppCompatActivity {

    private ActivityMoreinfoBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMoreinfoBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        BottomNavigationView navView = findViewById(R.id.nav_view);
        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        AppBarConfiguration appBarConfiguration = new AppBarConfiguration.Builder(
                R.id.navigation_home, R.id.navigation_dashboard, R.id.navigation_notifications,R.id.navigation_notifications)
                .build();
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_activity_moreinfo);
        NavigationUI.setupActionBarWithNavController(this, navController, appBarConfiguration);
        NavigationUI.setupWithNavController(binding.navView, navController);


        navView.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()) {
                    case R.id.navigation_home:
                        return true;
                    case R.id.navigation_t:
                        Intent in = new Intent(getApplicationContext(),VIEWTUTOR.class);
                        startActivity(in);
                        return true;
                    case R.id.navigation_dashboard:
                        // Handle navigation_dashboard click
//                        navController.navigate(R.id.navigation_dashboard);
                        Intent ik = new Intent(getApplicationContext(),internalmark.class);
                        startActivity(ik);
                        return true;
                    case R.id.navigation_notifications:
                        // Handle navigation_notifications click
//                        navController.navigate(R.id.navigation_notifications);
                        Intent ikk = new Intent(getApplicationContext(),attendencenew.class);
                        startActivity(ikk);
                        return true;
                    case R.id.navigation_mark:
                        // Handle navigation_notifications click
//                        navController.navigate(R.id.navigation_notifications);
                        Intent ikkk = new Intent(getApplicationContext(),VIEWSEMRESULTS.class);
                        startActivity(ikkk);
                        return true;

                }
                return false;
            }
        });


    }

}