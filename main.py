from graph import app

result = app.invoke({"message": "Tuhin!"})
print(result["message"])

png_data = app.get_graph().draw_mermaid_png()

# Specify the output filepath
out_file = "graph.png"

# Write to disk
with open(out_file, "wb") as f:
    f.write(png_data)

print(f"Saved graph image to {out_file}")