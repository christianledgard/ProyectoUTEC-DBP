package cs2901.utec.chat_mobile;

import android.content.Context;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RelativeLayout;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;


public class MyChampionshipAdapter extends RecyclerView.Adapter<MyChampionshipAdapter.ViewHolder> {
    public JSONArray elements;
    private Context context;
    public String userFromId;

    public MyChampionshipAdapter(JSONArray elements, Context context){
        this.elements = elements;
        this.context = context;
        //this.userFromId = userFromId;
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView first_line, second_line;
        RelativeLayout container;

        public ViewHolder(View itemView) {
            super(itemView);
            first_line = itemView.findViewById(R.id.element_view_first_line);
            second_line = itemView.findViewById(R.id.element_view_second_line);
            container = itemView.findViewById(R.id.element_view_container);
        }
    }

    @NonNull
    @Override
    public MyChampionshipAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.element_view,parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        try {
            JSONObject element = elements.getJSONObject(position);
            String subtitle = element.getString("category")+" - "+element.getString("location");
            subtitle = subtitle.substring(0,1).toUpperCase() + subtitle.substring(1);
            final String title = element.getString("title");
            final String championship_id = element.getString("id");
            final String category = element.getString("category");
            final String description = element.getString("description");
            final String endDate = element.getString("endDate");
            final String location = element.getString("location");
            final String price = element.getString("price");
            final String startDate = element.getString("startDate");
            holder.first_line.setText(title);
            holder.second_line.setText(subtitle);

            holder.container.setOnClickListener(new View.OnClickListener(){

                @Override
                public void onClick(View v) {
                    Intent goToMessage = new Intent(context, EventsActivity.class);
                    goToMessage.putExtra("championship_id", championship_id);
                    goToMessage.putExtra("category", category);
                    goToMessage.putExtra("description", description);
                    goToMessage.putExtra("endDate", endDate);
                    goToMessage.putExtra("location", location);
                    goToMessage.putExtra("price", price);
                    goToMessage.putExtra("startDate", startDate);
                    goToMessage.putExtra("title", title);
                    context.startActivity(goToMessage);
                }

            });

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    @Override
    public int getItemCount() {
        return elements.length();
    }
}
