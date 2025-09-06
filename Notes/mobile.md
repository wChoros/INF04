# Mobilki
## delete purple buttons
```xml


<!--- old --->
<style name="Base.Theme.Mobilka" parent="Theme.Material3.DayNight.NoActionBar">

<!--- new --->
<style name="Base.Theme.Mobilka" parent="Theme.AppCompat.Light.NoActionBar">

```

## Linear layout orientation
```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
>
```

## Onclick
```java
Button button= (Button) findViewById(R.id.standingsButton);
button.setOnClickListener(new View.OnClickListener() {
    public void onClick(View v) {
        startActivity(new Intent(MainActivity.this,StandingsActivity.class));
    }
});
```
