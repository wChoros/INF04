package com.example.mobilka;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.SeekBar;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        ListView listView1 = findViewById(R.id.animal_list);
        SeekBar seekBar1 = findViewById(R.id.age_bar);
        EditText name = findViewById(R.id.name);
        TextView age = findViewById(R.id.age_text);
        Button submit_btn = findViewById(R.id.submit);
        TextView visit_details = findViewById(R.id.visit_details);
        TextView purpose = findViewById(R.id.purpose);
        TextView time = findViewById(R.id.time);
        final String[] currSpiece = {"Pies"};

        seekBar1.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean
                    fromUser) {
                age.setText("Ile ma lat? " + progress);
            }
        });
        seekBar1.setMax(18);

        ArrayList<String> tablica_elementow = new ArrayList<String>();
        tablica_elementow.add("Pies");
        tablica_elementow.add("Kot");
        tablica_elementow.add("Świnka Morska");


        ArrayAdapter<String> arrayAdapter = new ArrayAdapter<>(this,
                R.layout.list_item, R.id.list_item_text, tablica_elementow);
        listView1.setAdapter(arrayAdapter);


        listView1.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            public void onItemClick(AdapterView<?> myAdapter, View myView, int
                    myItemInt, long mylng) {
                String elementWybrany = (String) listView1.getItemAtPosition(myItemInt);
                currSpiece[0] = elementWybrany;
                switch (elementWybrany) {
                    case ("Pies"): {
                        seekBar1.setMax(18);
                        break;
                    }
                    case ("Kot"): {
                        seekBar1.setMax(20);
                        break;
                    }
                    case ("Świnka Morska"): {
                        seekBar1.setMax(9);
                        break;
                    }
                }
            }
        });

        submit_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                visit_details.setText(name.getText() + ", " + currSpiece[0] + ", " + age.getText() + ", " + purpose.getText() + ", " + time.getText());
            }
        });

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }
}