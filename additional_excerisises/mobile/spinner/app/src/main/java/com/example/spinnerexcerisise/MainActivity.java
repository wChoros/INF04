package com.example.spinnerexcerisise;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {

    private final String[] voivodeships = {
            "Dolnośląskie",
            "Kujawsko-Pomorskie",
            "Lubelskie",
            "Lubuskie",
            "Łódzkie",
            "Małopolskie",
            "Mazowieckie",
            "Opolskie",
            "Podkarpackie",
            "Podlaskie",
            "Pomorskie",
            "Śląskie",
            "Świętokrzyskie",
            "Warmińsko-Mazurskie",
            "Wielkopolskie",
            "Zachodniopomorskie"
    };

    protected static int numberOfChoices = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        Spinner voivodeshipsSpinner = findViewById(R.id.voivodeships_spinner);

        voivodeshipsSpinner.setOnItemSelectedListener(this);

        ArrayAdapter<String> ad = new ArrayAdapter<>(
                this,
                android.R.layout.simple_spinner_item,
                voivodeships
        );

        ad.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        voivodeshipsSpinner.setAdapter(ad);
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        // Make toast of the name of the course which is selected in the spinner

//        Toast.makeText(getApplicationContext(), voivodeships[position], Toast.LENGTH_SHORT).show();
        if (numberOfChoices>0) {
            TextView displayer = findViewById(R.id.displayer);
            displayer.setText("Wybrałeś " + voivodeships[position]);
        }
            numberOfChoices++;

    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {
        // No action needed when no selection is made
    }
}