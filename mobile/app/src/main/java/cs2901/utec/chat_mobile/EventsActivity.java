package cs2901.utec.chat_mobile;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.widget.TextView;


public class EventsActivity extends AppCompatActivity {

    RecyclerView mRecyclerView;
    RecyclerView.Adapter mAdapter;
    String championship_id;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_message);
        String title = getIntent().getExtras().get("title").toString();
        championship_id = getIntent().getExtras().get("championship_id").toString();
        String category = getIntent().getExtras().get("category").toString();
        String description = getIntent().getExtras().get("description").toString();
        String endDate = getIntent().getExtras().get("endDate").toString();
        String location = getIntent().getExtras().get("location").toString();
        String price = getIntent().getExtras().get("price").toString();
        String startDate = getIntent().getExtras().get("startDate").toString();
        setTitle(title);
        mRecyclerView = findViewById(R.id.main_recycler_view);


        final TextView textViewTitle = (TextView)findViewById(R.id.title);
        final TextView textViewCategory = (TextView)findViewById(R.id.category);
        final TextView textViewDescription = (TextView)findViewById(R.id.description);
        final TextView textViewEndDate = (TextView)findViewById(R.id.endDate);
        final TextView textViewStartDate = (TextView)findViewById(R.id.startDate);
        final TextView textViewLocation = (TextView)findViewById(R.id.location);
        final TextView textViewPrice = (TextView)findViewById(R.id.price);


        textViewTitle.setText(title);
        textViewCategory.setText(category);
        textViewDescription.setText(description);
        textViewEndDate.setText(endDate);
        textViewStartDate.setText(startDate);
        textViewLocation.setText(location);
        textViewPrice.setText(price);


    }


    public void onBtnInscription(View v) {
        Intent intent = new Intent(this, InscripcionActivity.class);
        intent.putExtra("championship_id", championship_id);
        startActivity(intent);
    }

}
