package com.example.departmentmanagement;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class customviewsemresults extends BaseAdapter {

    String[] id,ti,sem,typ,file;
    private Context context;

    public customviewsemresults(Context applicationContext, String[] id, String[] sem, String[] typ, String[] file) {
        this.context = applicationContext;
        this.id = id;
        this.sem = sem;
        this.typ = typ;
        this.file = file;


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
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null)
        {
            gridView=new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView=inflator.inflate(R.layout.activity_customviewsemresults,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView82);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView90);
        ImageView im=(ImageView) gridView.findViewById(R.id.imageView9);
        im.setTag(i);
        im.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int pos = (int) view.getTag();
                SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
                String url=sh.getString("url","");
                String value=url+file[pos];
                Intent intent=new Intent(Intent.ACTION_VIEW, Uri.parse(value));
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(intent);
            }
        });

        tv1.setTextColor(Color.BLACK);
        tv2.setTextColor(Color.BLACK);


        tv1.setText(sem[i]);
        tv2.setText(typ[i]);
        return gridView;


    }
}