Categorical Plots
=================

.. code-block:: python
   :linenos:

    import bokehBorn as bb
    from bokeh.io import output_notebook
    output_notebook()


Bar Plots
---------


**Draw Vertical Bar**

Draw a set of vertical bar plots grouped by a categorical variable:

.. code-block:: python
   :linenos:

    bb.barplot(x="day", y="total_bill", data=tips)


.. image:: 3_1_bar_plot.png
  :width: 600


**Draw Horizontal Bar**

Draw a set of horizontal bars automatically with change of axis

.. code-block:: python
   :linenos:

    bb.barplot(x="tip", y="day", data=tips)


.. image:: 3_1_bar_plot.png
  :width: 600


**Control Orders**

Control bar order by passing an explicit order:

.. code-block:: python
   :linenos:

    bb.barplot(x="time", y="tip", data=tips,order=["Lunch", "Dinner"])


.. image:: 3_1_bar_plot.png
  :width: 600


**Set Desired Estimator**

For example, use median as the estimate of central tendency:

.. code-block:: python
   :linenos:

    from numpy import median
    bb.barplot(x="day", y="tip", data=tips, estimator=median)


.. image:: 3_1_bar_plot.png
  :width: 600


**Choose Palettes**

Use a different color palette for the bars:

.. code-block:: python
   :linenos:

    bb.barplot(x= "day", y="total_bill", data=tips, palette="Blues_d")


.. image:: 3_1_bar_plot.png
  :width: 600


**Set Specific Color**

Plot all bars in a single color:

.. code-block:: python
   :linenos:

    bb.barplot(x= "day", y="total_bill", data=tips, color="salmon")


.. image:: 3_1_bar_plot.png
  :width: 600


**Use Hue for Visualization**

Draw a set of vertical bars with nested grouping by a two variables:

.. code-block:: python
   :linenos:

    bb.barplot(x="day", y="total_bill", hue="sex", data=tips)


.. image:: 3_1_bar_plot.png
  :width: 600


.. code-block:: python
   :linenos:

    bb.barplot(x="day", y="total_bill", hue="smoker", data=tips)


.. image:: 3_1_bar_plot.png
  :width: 600


**Change Plot Properties**

Change different plot properties such as plot_width:

.. code-block:: python
   :linenos:

    bb.barplot(x="day", y="total_bill", data=tips, plot_width=800)


.. image:: 3_1_bar_plot.png
  :width: 600

For example, add plot title:

.. code-block:: python
   :linenos:

    bb.barplot(x="day", y="total_bill", data=tips,  plot_title="Awesome Plot Title")


.. image:: 3_1_bar_plot.png
  :width: 600


**And Many More**

Change the other aesthetics of the plot as key word arguments as available in `bokeh.plotting.figure.vbar` , such as changing alpha of the plot. List of all the aesthetics properties :: https://docs.bokeh.org/en/latest/docs/reference/plotting.html#bokeh.plotting.figure.Figure.vbar

.. code-block:: python
   :linenos:

    bb.barplot(x="day", y="total_bill", data=tips, alpha=0.3)


.. image:: 3_1_bar_plot.png
  :width: 600