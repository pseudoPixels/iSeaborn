iSeaborn Gallery
================

Vertical Bar Plot
-----------------
Draw a set of vertical bar plots grouped by a categorical variable:

.. code-block:: python
   :linenos:
   :emphasize-lines: 5

    import iSeaborn as isn
    from bokeh.plotting import output_file, save

    tips = isn.load_dataset("tips")
    fig = isn.barplot(x="day", y="total_bill", data=tips)

    output_file("verticalBarPlot.html")
    save(fig)


.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/basicBarPlot.html


Choose from Interactive Tools
-----------------------------
Choose the required interactive tools for visualization by passing value to tools options.
Default tools are "pan,box_select,wheel_zoom,box_zoom,reset,save"

.. code-block:: python
   :linenos:
   :emphasize-lines: 5

   import iSeaborn as isn
   from bokeh.plotting import output_file, save

   tips = isn.load_dataset("tips")
   fig = isn.barplot(x="day", y="total_bill", data=tips, tools="pan, save")

   output_file("chooseInteractiveTools.html")
   save(fig)


.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/chooseInteractiveTools.html



Control Plot Orders
-------------------
Control bar order by passing an explicit order:

.. code-block:: python
   :linenos:
   :emphasize-lines: 5

   import iSeaborn as isn
   from bokeh.plotting import output_file, save

   tips = isn.load_dataset("tips")
   fig = isn.barplot(x="time", y="tip", data=tips,order=["Lunch", "Dinner"])

   output_file("chooseInteractiveTools.html")
   save(fig)

.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/controlPlotOrders.html


Draw Horizontal Bar
-------------------
Draw a set of horizontal bars automatically with change of axis.

.. code-block:: python
   :linenos:
   :emphasize-lines: 5

   import iSeaborn as isn
   from bokeh.plotting import output_file, save

   tips = isn.load_dataset("tips")
   fig = isn.barplot(x="tip", y="day", data=tips)

   output_file("drawHorizontalBar.html")
   save(fig)


.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/horizontalBar.html


