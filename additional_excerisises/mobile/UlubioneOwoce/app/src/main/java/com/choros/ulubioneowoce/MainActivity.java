package com.choros.ulubioneowoce;

import android.graphics.Color;
import android.os.Bundle;
import android.widget.*;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private static final int MAX_FRUITS = 10;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        ArrayList<String> fruits = new ArrayList<>();

        ListView listOfFruits = findViewById(R.id.listOfFruits);
        TextView fruitName = findViewById(R.id.fruitName);
        Button addFruitBtn = findViewById(R.id.fruitButton);

        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, R.layout.list_item, fruits);
        listOfFruits.setAdapter(adapter);

        // Add new fruit button
        addFruitBtn.setOnClickListener(v -> {
            String newFruit = fruitName.getText().toString().trim();

            if (newFruit.isEmpty()) {
                Toast.makeText(this, "Nie podano nazwy owocu", Toast.LENGTH_SHORT).show();
                return;
            }

            if (fruits.size() >= MAX_FRUITS) {
                Toast.makeText(this, "Lista jest pełna!", Toast.LENGTH_SHORT).show();
                return;
            }

            fruits.add(newFruit);
            adapter.notifyDataSetChanged();
            updateListColor(listOfFruits, fruits.size());
        });

        // Show toast when an item is clicked
        listOfFruits.setOnItemClickListener((parent, view, position, id) -> {
            String clickedFruit = fruits.get(position);
            Toast.makeText(this, "Kliknięto: " + clickedFruit, Toast.LENGTH_SHORT).show();
        });

        updateListColor(listOfFruits, fruits.size());
    }

    private void updateListColor(ListView list, int size) {
        int color;
        if (size >= MAX_FRUITS) {
            color = Color.RED;
        } else if (size % 2 == 0) {
            color = Color.BLUE;
        } else {
            color = Color.GREEN;
        }
        list.setBackgroundColor(color);
    }
}
