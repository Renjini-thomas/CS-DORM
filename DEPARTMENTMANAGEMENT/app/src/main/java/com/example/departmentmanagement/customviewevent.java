package com.example.departmentmanagement;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class customviewevent extends BaseAdapter {
    String[] id,en,ep,ed;
    private Context context;

    public customviewevent(Context applicationContext, String[] id, String[] en, String[] ep, String[] ed) {

        this.context = applicationContext;
        this.id = id;
        this.en = en;
        this.ep = ep;
        this.ed = ed;

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
            gridView=inflator.inflate(R.layout.activity_customviewevent,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView8);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView21);
        ImageView im=(ImageView) gridView.findViewById(R.id.imageView);

        tv1.setTextColor(Color.BLACK);


        tv1.setText(ed[i]);
        tv2.setText(en[i]);



        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String url=sh.getString("url","");

        Picasso.with(context).load(url+ep[i]). into(im);

        return gridView;


    }
}