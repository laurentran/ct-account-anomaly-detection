--t0
SELECT
p.ct_planid, 
p.ct_custodianname,  
p.ct_discretionarytypename,
p.ct_erisaname,      
p.ct_modeltypeidname,
p.ct_plantypename,
aa.ct_assetclassidname,
aa.ct_investmentidname,
aa.ct_plantype,
aa.ct_allocationname,
i.ct_strategyid,
i.ct_macroassetclass,
i.ct_investmenttype,
ct_value
,ct_valuedate
FROM [plan] AS p 
inner join [allocation_asset] AS aa 
ON p.ct_planid = aa.[ct_planid] 
inner join [dbo].[investments] AS i
ON aa.ct_investmentid = i.ct_investmentid 
 inner join [dbo].[marketvalue_allocation_asset] maa ON 
  aa.ct_allocationassetid1 = maa.ct_assetallocationid
WHERE 
 maa.ct_valuedate='2017-09-30 00:00:00.000'
GROUP BY 
p.ct_planid, 
p.ct_custodianname,  
p.ct_discretionarytypename,
p.ct_erisaname,      
p.ct_modeltypeidname,
p.ct_plantypename,
aa.ct_assetclassidname,
aa.ct_investmentidname,
aa.ct_plantype,
aa.ct_allocationname,
i.ct_strategyid,
i.ct_macroassetclass,
i.ct_investmenttype,
aa.statecodename,
maa.ct_assetallocationid,
maa.ct_value
,maa.ct_valuedate
ORDER BY 
p.ct_planid 


--t1
SELECT
p.ct_planid, 
p.ct_custodianname,  
p.ct_discretionarytypename,
p.ct_erisaname,      
p.ct_modeltypeidname,
p.ct_plantypename,
aa.ct_assetclassidname,
aa.ct_investmentidname,
aa.ct_plantype,
aa.ct_allocationname,
i.ct_strategyid,
i.ct_macroassetclass,
i.ct_investmenttype,
ct_value
,ct_valuedate
FROM [plan] AS p 
inner join [allocation_asset] AS aa 
ON p.ct_planid = aa.[ct_planid] 
inner join [dbo].[investments] AS i
ON aa.ct_investmentid = i.ct_investmentid 
 inner join [dbo].[marketvalue_allocation_asset] maa ON 
  aa.ct_allocationassetid1 = maa.ct_assetallocationid
WHERE 
  maa.ct_valuedate='2017-12-31 00:00:00.000'
GROUP BY 
p.ct_planid, 
p.ct_custodianname,  
p.ct_discretionarytypename,
p.ct_erisaname,      
p.ct_modeltypeidname,
p.ct_plantypename,
aa.ct_assetclassidname,
aa.ct_investmentidname,
aa.ct_plantype,
aa.ct_allocationname,
i.ct_strategyid,
i.ct_macroassetclass,
i.ct_investmenttype,
aa.statecodename,
maa.ct_assetallocationid,
maa.ct_value
,maa.ct_valuedate
ORDER BY 
p.ct_planid 


