package com.example.departmentmanagement;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class customviewmark extends BaseAdapter {
    String[] id,sub,totatt,att,mark;

    private final Context context;


    public customviewmark(Context applicationContext, String[] id, String[] sub,  String[] mark) {


        this.context = applicationContext;
        this.id = id;
        this.sub = sub;

        this.mark = mark;
    }


    @Override
    public int getCount() {
        return id.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {

        LayoutInflater inflator = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if (view == null) {
            gridView = new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView = inflator.inflate(R.layout.activity_customviewmark, null);

        } else {
            gridView = (View) view;

        }
        TextView tv1 = (TextView) gridView.findViewById(R.id.textView11);

        TextView tv4 = (TextView) gridView.findViewById(R.id.textView12);


        tv1.setTextColor(Color.BLACK);


        tv1.setText(sub[i]);

        tv4.setText(mark[i]);


        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(context);
        String url = sh.getString("url", "");

        //Picasso.with(context).load(url + ep[i]).into(im);

        return gridView;
    }

}