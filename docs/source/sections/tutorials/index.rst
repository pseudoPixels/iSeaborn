Tutorial
========

Bar Plots
#########

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


Set Desired Estimator
---------------------
For example, use median as the estimate of central tendency

.. code-block:: python
   :linenos:
   :emphasize-lines: 3, 6

   import iSeaborn as isn
   from bokeh.plotting import output_file, save
   from numpy import median

   tips = isn.load_dataset("tips")
   fig = isn.barplot(x="day", y="tip", data=tips, estimator=median)

   output_file("setDesiredEstimator.html")
   save(fig)


.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/setDesiredEstimator.html



Choose From Color Palettes
---------------------------
Use a different color palette for the bars:

.. code-block:: python
   :linenos:
   :emphasize-lines: 5

   import iSeaborn as isn
   from bokeh.plotting import output_file, save

   tips = isn.load_dataset("tips")
   fig = isn.barplot(x= "day", y="total_bill", data=tips, palette="Blues_d")

   output_file("chooseFromColorPalletes.html")
   save(fig)


.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/chooseFromColorPalletes.html


Set Specific Color
---------------------------
Plot all bars in a single color:

.. code-block:: python
   :linenos:
   :emphasize-lines: 5

   import iSeaborn as isn
   from bokeh.plotting import output_file, save

   tips = isn.load_dataset("tips")
   fig = isn.barplot(x= "day", y="total_bill", data=tips, color="salmon")

   output_file("setPrefferedColor.html")
   save(fig)


.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/setPrefferedColor.html


Use Hue for Visualization
---------------------------
Draw a set of vertical bars with nested grouping by a two variables:

.. note:: Click the legend text to view only a selected category.

.. code-block:: python
   :linenos:
   :emphasize-lines: 5

   import iSeaborn as isn
   from bokeh.plotting import output_file, save

   tips = isn.load_dataset("tips")
   fig = isn.barplot(x="day", y="total_bill", hue="sex", data=tips)

   output_file("useHue.html")
   save(fig)



.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/useHue.html


Change Plot Properties
---------------------------
Change different plot properties:

.. code-block:: python
   :linenos:
   :emphasize-lines: 5,6,7

   import iSeaborn as isn
   from bokeh.plotting import output_file, save

   tips = isn.load_dataset("tips")
   fig = isn.barplot(x="day", y="total_bill", data=tips,
                     plot_width=600, plot_height=200,
                     plot_title="Awesome Plot Title")

   output_file("setPlotProps.html")
   save(fig)



.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/setPlotProps.html


And More
---------------------------
Change the other aesthetics of the plot as key word arguments as available in `bokeh.plotting.figure.vbar` , such as changing alpha of the plot.

.. note:: List of all the aesthetics properties :: https://docs.bokeh.org/en/latest/docs/reference/plotting.html#bokeh.plotting.figure.Figure.vbar

.. code-block:: python
   :linenos:
   :emphasize-lines: 5

   import iSeaborn as isn
   from bokeh.plotting import output_file, save

   tips = isn.load_dataset("tips")
   fig = isn.barplot(x="day", y="total_bill", data=tips, alpha=0.3)

   output_file("vbarProps.html")
   save(fig)



.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/vbarProps.html
