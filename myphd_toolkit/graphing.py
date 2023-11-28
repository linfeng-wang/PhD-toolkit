import itertools
import plotly.graph_objects as go

def piechart(lin_count, highest=True):
    total = sum(lin_count.values())
    if highest:
        lin_count = dict(sorted(lin_count.items(), key=lambda item: item[1], reverse=True))
        rest_count = list(lin_count.values())[10:-1]
        lin_count = dict(itertools.islice(lin_count.items(),10))
        lin_count["Rest"] = sum(rest_count)

    labels = []
    sizes = []
    for x, y in lin_count.items():
        labels.append(x)
        sizes.append(y/total)
    # print(lin_count)

    fig = go.Figure(data=[go.Pie(labels=labels,
                                values=sizes)])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20)
    fig.show()


