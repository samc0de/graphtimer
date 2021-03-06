from .graphtimer import CATEGORY10


class MatPlotLib:
    def _graph_times(self, graph, values, errors, domain, colors, error, fmt):
        for values, errors, color in zip(values, errors, colors):
            if error:
                errors = zip(*errors)
                for error in errors:
                    lower, upper = zip(*error)
                    graph.fill_between(
                        domain, upper, lower, facecolor=color, edgecolor=None, alpha=0.1
                    )
            yield graph.plot(domain, values, fmt, color=color)[0]

    def graph(
        self,
        graph,
        values,
        errors,
        domain,
        *,
        functions=None,
        colors=CATEGORY10,
        title=None,
        legend=True,
        error=True,
        x_label="Input",
        y_label="Time [s]",
        fmt="-"
    ):
        lines = list(
            self._graph_times(graph, values, errors, domain, colors, error, fmt)
        )
        if x_label is not None:
            graph.set_xlabel(x_label)
        if y_label is not None:
            graph.set_ylabel(y_label)
        if title is not None and hasattr(graph, "set_title"):
            graph.set_title(title)
        if legend and functions is not None and hasattr(graph, "legend"):
            legend = [
                getattr(fn, "__qualname__", None) or fn.__name__ for fn in functions
            ]
            graph.legend(lines, legend, loc=0)
        return lines
