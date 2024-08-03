import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [85, 92, 78, 88]
}

df = pd.DataFrame(data)

styled_df = df.style.set_properties(**{
    'background-color': 'lightyellow',
    'color': 'black',
    'border-color': 'black'
})

def color_score(val):
    color = 'green' if val > 90 else 'red'
    return f'background-color: {color}'

styled_df = df.style.applymap(color_score, subset=['Score'])

styled_df = df.style.highlight_max(subset=['Score'], color='lightgreen')
styled_df = styled_df.highlight_min(subset=['Score'], color='lightcoral')

styled_df = df.style.set_table_styles(
    [{'selector': 'tr:hover',
      'props': [('background-color', 'yellow')]}]
)

styled_df

html = styled_df.render()
with open('styled_df.html', 'w') as f:
    f.write(html)

