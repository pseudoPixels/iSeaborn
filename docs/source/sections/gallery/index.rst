iSeaborn Gallery
================

Vertical Bar Plot
-----------------

.. code-block:: python
   :linenos:

    import bokehBorn as bb
    from bokeh.plotting import output_file, save

    tips = bb.load_dataset("tips")
    fig = bb.barplot(x="day", y="total_bill", data=tips)

    output_file("basicBarPlot.html")
    save(fig)


.. raw:: html
   :file: ../../../_static/outputs_interactive_plots/basicBarPlot.html