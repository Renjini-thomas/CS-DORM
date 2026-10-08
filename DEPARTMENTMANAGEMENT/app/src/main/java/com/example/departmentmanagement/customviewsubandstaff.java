package com.example.departmentmanagement;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.net.Uri;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class customviewsubandstaff extends BaseAdapter {
    String[] id,staffphoto,staffname,sub,number,syll;
    private Context context;

    public customviewsubandstaff(Context applicationContext, String[] id, String[] staffphoto, String[] staffname, String[] sub, String[] number, String[] syll) {
        this.context = applicationContext;
        this.id=id;
        this.staffphoto=staffphoto;
        this.staffname=staffname;
        this.sub=sub;
        this.number = number;
        this.syll = syll;
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
            gridView=inflator.inflate(R.layout.activity_customviewsubandstaff,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView27);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView28);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView89);
        tv3.setTag(i);
        tv3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int pos = (int) view.getTag();
                SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
                String url=sh.getString("url","");
                String value=url+syll[pos];
                Intent intent=new Intent(Intent.ACTION_VIEW, Uri.parse(value));
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(intent);
            }
        });
        ImageView im=(ImageView) gridView.findViewById(R.id.imageView3);

        Button b = (Button)gridView.findViewById(R.id.button3);
        b.setTag(i);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int pos = (int) view.getTag();
                Intent whatsapp = new Intent(Intent.ACTION_VIEW, Uri.parse("https://api.whatsapp.com/send?phone=+91"+number[pos]));
                whatsapp.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(whatsapp);

            }
        });
        Button b1 = (Button)gridView.findViewById(R.id.button8);


        SharedPreferences sh1  = PreferenceManager.getDefaultSharedPreferences(context);
        if(sh1.getString("t","").equalsIgnoreCase("student")) {
            b1.setVisibility(View.VISIBLE);
        }
        else
        {
            b1.setVisibility(View.INVISIBLE);

}





        b1.setTag(i);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {


                int pos = (int) view.getTag();
                SharedPreferences sh  = PreferenceManager.getDefaultSharedPreferences(context);
                SharedPreferences.Editor editor = sh.edit();
                editor.putString("mid",id[pos]);
                editor.apply();
                Intent in = new Intent(context,VIEWMWTERIAL.class);
                in.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(in);
            }
        });


        tv1.setTextColor(Color.BLACK);


        tv1.setText(sub[i]);
        tv2.setText(staffname[i]);
//        tv3.setText(syll[i]);



        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String url=sh.getString("url","");

        Picasso.with(context).load(url+staffphoto[i]). into(im);

        return gridView;


    }
}

