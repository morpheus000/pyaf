
import pyaf.ForecastEngine as autof
import pyaf.Bench.TS_datasets as tsds


b1 = tsds.load_ozone()
df = b1.mPastData

lEngine = autof.cForecastEngine()
lEngine

H = b1.mHorizon;
lEngine.mOptions.mFilterSeasonals = False;
lEngine.mOptions.mParallelMode = False;
lEngine.mOptions.mDebugPerformance = True;
lEngine.train(df , b1.mTimeVar , b1.mSignalVar, H);
lEngine.getModelInfo();
print(lEngine.mSignalDecomposition.mTrPerfDetails.head());

